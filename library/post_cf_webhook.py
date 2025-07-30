data = {
    "job_id":   task['id'],
    "srpm":     task['params'][0],
    "arch":     task['arch'],          # Koji passes this in every build task
    "oreon":    task['tag_name'],      # or parse from build target
    "callback": f"{ALBS_API}/internal/task/{task['id']}/done"
}
requests.post(os.environ["CF_ALBS_WEBHOOK"], json=data, timeout=10)