# openshift-algorithm

My own algorithms for my own needs.

Good chunk of the OpenShift/Travis CI algos I wrote:

## OpenShift Algo by Me

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

## Travis CI Queue Algo by me 

```python
# travis queue algorithm 
while travis_queue:
    target, task, interval, cur_id = self.task_q[0]
    self.notify.wait(max(target - time.time(), 0))
    if self.stopping:
        return
        # look out for heaps 
    self.notify.clear()
    target, task, interval, cur_id = heap.heappop(self.task_q)
    if cur_id in self.removed_ids:
        self.removed_ids.remove(cur_id)
        continue
    done = task()
    if not done:
        heapq.heappush(
        self.task_q, (target + interval, task, interval, cur_id))
     cur_id = self._next_id
        cur_batch_size = min(n_samples, len(self) - self._next_id)
        assert cur_batch_size > 0
        # get the range 
        for x in range(0, squares):
			self.button_states[int(math.floor(x / 8))][x % 8] = 1
                if self.parent.active_page == 2:
			for x in range(0, 8):
				for y in range(0, 8):
					lp.LedCtrlRaw(button_defs.row[x][y], 0, 3*self.button_states[x][y])
         # look for build batches going out, this will keep checking (looping via the cron i setup earlier)
        self._next_id += cur_batch_size 
        result = {}
        for key in self.data_map:
            result[key] = self.data_map[key][cur_id: cur_id + cur_batch_size]
            assert len(result[key] == cur_batch_size)
        return cur_batch_size, result
   ```
