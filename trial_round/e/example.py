from collections import deque

def main():
  connections = []
  number_of_requests = 0
  download_requests = []
  relations = {}
  components = {}
  
  with open('input.txt') as fp:
    for i, line in enumerate(fp):
      if i == 0:
        number_of_connections = int(line)
      if 1 <= i <= number_of_connections:
        connections.append(line.strip().split())
      if i == number_of_connections+1:
        number_of_requests = int(line)
      if number_of_connections + 2 <= i <= number_of_connections + 3 + number_of_requests * 2:
        download_requests.append(line.strip().split())

  for connection in connections:
    add_connecton(connection, relations)

  build_components(relations, components)

  for _ in range(1, number_of_requests + 1):
    first_string = download_requests.pop(0)
    from_servers = download_requests.pop(0)
    to_server = first_string[0]
    check(from_servers, to_server, components)

def add_connecton(connection, relations):
  if relations.get(int(connection[0])): relations[int(connection[0])].append(int(connection[1]))
  else: relations[int(connection[0])] = [int(connection[1])]

  if relations.get(int(connection[1])): relations[int(connection[1])].append(int(connection[0]))
  else: relations[int(connection[1])] = [int(connection[0])]

def build_components(relations, components):
  componentCount = 0
  for relation_key in relations:
    if components.get(relation_key): continue
    componentCount += 1

    search_queue = deque()
    search_queue += relations[relation_key]
    components[relation_key] = componentCount
    
    while search_queue:
      queue_item = search_queue.popleft()
      if queue_item in relations:
        for relation_item in relations[queue_item]:
          if components.get(relation_item):
            if not components.get(queue_item):
              components[queue_item] = componentCount
            continue
          search_queue.append(relation_item)
          components[relation_item] = componentCount
 
def check(servers, to_server, components):
  for_download = []
  for server in servers:
    if components[int(server)] == components[int(to_server)]:
      for_download.append(int(server))
  print(str(len(for_download)) + ' ' + str(for_download).strip('[]').replace(',', ''))

main()