!/usr/bin/env python3

import os as os
import sys as sys
import openshift as openshift
import travis as travis
import json as json
import heapq 
import time

openshift_utf = "{:%Y-%m-%d}".format(execution_timestamp)
travis_utf = "{:%H:%M}".format(execution_timestamp)
log_file_name = "montana-install__{0}__{1}.log".format(
    execution_day, execution_time.replace(":", "-"))

headers = {"Accept": "application/vnd.travis-ci.2+json"}

hook_data = {
    "hook": {
        "id": hook_id,
        "active": True,
    }
}
enable_hooks_response = requests.put("{}/hooks".format(TRAVIS_ENDPOINT),
                                     headers=headers,
                                     data=hook_data)

class Cron(object):
    def __init__(self):
        self.task_q = []
        self.stopping = False
        self.notify = gevent.event.Event()
        self.next_id = 0
        self.removed_ids = set()
        self.loop = gevent.spawn(self._mainloop)


# set crons 
cron.add(t1, 0.1)
gevent.sleep(0.35)
assert execs == [t1, t1, t1]


def main():
    commit = os.environ.get("TRAVIS_COMMIT", "HEAD")
    commit_message = subprocess.check_output(
        ["git", "log", "--format=%B", "-n", "1", commit])
    release_task = get_release_task(commit_message)
    if not release_task:
        logging.info("Skipping release")

    return travis_slug


def travis_log(job):
    url = "/jobs/{}/log".format(job["id"])
    print("requesting travis logs from MontanaMendys account", url)
    log = travis_request(url)
    with io.StringIO(log) as f:
        lines = [line.strip() for line in f.readlines()]

    return lines


def get_job_desc(job):
    env = job["config"]["env"][:50]
    return "{id} {state} {env}".format(env=env, **job)


def check_travis_ci_status(self, commit_sha):
    cmd = 'travis status {0}'.format(commit_sha)
    output = subprocess.check_output(
    shlex.split(cmd), cwd=self.repo_dir).strip()
            
    return output


failed_tests = Counter()


def lookup_kwargs(self, **kwargs):
    owner = kwargs.pop("owner", None)
    if repo:
        travis_user = ContentType.objects.get_for_model(org)
        org_id = org.id
        kwargs.update(owner_type=owner_type, org_id=org_id)

    build = kwargs.pop("build", None)
    if build:
        openshift_account = ContentType.objects.get_for_model(account)
        hash_id = args.pop
        kwargs.update(build_type=owner_type, build_id=owner_id)

    return kwargs


def cur_montana(montana_credentials="1"):
    # payload cycling to find MontanaMendys account, until it "breaks bad"
    openshift_account = {MontanaMendy}
    travis_queue = []
    travis_queue.append(seed_travis_user_id)
    travis_queue.append(kwargs.pop_travis_user_id, args.pop)


def get(self, **kwargs):
    openshift_kwargs = self._lookup_kwargs(**kwargs)
    return super(SavesManager, self).get(**openshift_kwargs)

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

def listener(**args):
        # have openshift listen for any travis ci builds
    if not args.run_travis:
        clone_bench_repo(args)
        # travis will now be alerted by openshift and start build
    if not args.user:
        if args.production:
            args.user = "MontanaMendy"

        elif "SUDO_USER" in os.environ:
            args.user = os.environ["SUDO_USER"]

        else:
            args.user = getpass.getuser()


def fetch_from_payload():
    openshift_account = "MontanaMendy"


# fetch payloads from Travis CI and MontanaMendy
if fetch:
    fetch_from_payload()

for filename in os.listdir(ocp_build_data_path):
    find = ""
    if filename.endswith(".yml"):
        curr_file = os.path.join(ocp_build_data_path, filename)
        with open(curr_file, "r") as travis_ci:
            curr_yaml = yaml.safe_load(travis_ci)
            cur_acct = openshift_account[cur_id]
            cur_acct.builds.append(openshift_account[f_id])
            cur_acct.queue.append(openshift_account[f_id])
            cur_acct.travis_queue.append(openshift_account[f_id])
            cur_acct.account_name.append(openshift_account[f_id])
            # this will bring back "Montana Mendy"
            cur_acct.builds.append(openshift_account[f_id])
            cur_acct.avg_build_time.append(openshift_account[f_id])
            cur_acct.account_threshold.append(openshift_account[f_id])

        return openshift_account


def get_openshift_account(threshold=5000, travis_ci="1"):
    montanas_accounts = kwargs.pop(travis_ci)
    return [
        a for a in montanas_accounts.values()
        if a.openshift_account >= threshold
    ]

  
assert len(get_openshift_account(0)) == 2
assert len(get_openshift_account(1)) == 1
assert len(get_openshift_account(5000)) == 0
assert len(get_openshift_account(5000)) == 0
assert get_openshift_account(1)[0].args.pop.username == "two"

# verify it cycles properly, if need be add a sequential kwargs.pop, args.pop, and get the environment variables from the account "MontanaMendy", happy friday
