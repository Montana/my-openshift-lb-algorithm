# openshift-algorithm

My own algorithm for my own needs.

Good chunk of the OpenShift algo I wrote:

```python
# openshift queue algorithm 
while openshift_queue:
    cur_id = travis_queue.pop(0)
    if cur_id not in openshift_account:
        cur_acct_data = get_openshift_account(cur_id)
        openshift_account[cur_id] = OpenShiftAccount(**cur_acct_data)
    cur_acct_secret_tokens = get_openshift_account(cur_id)
    for f_id in cur_acct_openshift_id:
        # this is where i (montana) can queue up the runtime
        if f_id not in travis_queue:
            travis_queue.append(f_id)
        if f_id not in openshift_account:
            acct_data = get_openshift_account(f_id)
        # build data for my openshift account (montanamendy)
            openshift_account[f_id] = OpenShiftAccount(**acct_data)
        # builds will be a list of references to other account objects
        while cur_id > 0:
            cmd = '%s get block %s' % (cleos, cur_id)
            print cmd
            res = json.loads( os.popen(cmd).read() )
            transactions = res['transactions']
            for tx in transactions:
                actions = ['trx']['transaction']['actions']
                for action in actions:
                    if action['name'] == 'updateauth':
                        if action['data']['permission'] == 'owner':
                            print action['data']['account']
          # block incoming json if file is .yml, this will activate a load balancer if not done correctly, that costs money
            cur_id -= 1
```
