import time
from pygit2 import Repository, Signature, utils

# lookup head 
repo = Repository('test')
head = repo.lookup_reference('HEAD').resolve()
commit = repo[head.oid]
tree = commit.tree

# insert foo.txt in path/to/blob/foo.txt
root_oid = commit.tree.oid
node_oid = repo.create_blob('foo')
tree_oid = utils.tree_insert_node(repo, root_oid, node_oid, 'path/to/blob/foo.txt')

# commit everything
author = committer = Signature('foo bar', 'foo@bar.de', int(time.time()), 120)
repo.create_commit(
  'HEAD',
  author,
  committer,
  'copied foo to path/to/blob/foo.txt',
  tree_oid,
  [commit.oid]
)
