from os import path
if path.exists("env.py"):
  import env 

os.environ["STRIPE_PUBLIC_KEY"] = "pk_test_51IgFirCIA5Lh0GU7IxROVnj3zw5ty4feoYXFRug5WWlQTFFYInRC0vNpuHCKyN4k327pzU9sCoP972PDrTz9eRCV00B6XZks0j"
os.environ["STRIPE_SECRET_KEY"] = "sk_test_51IgFirCIA5Lh0GU7EF9oJNEjVidfxFFitAbKUSv6j7zHbE2rRpe5EmDiwJ8m6WMfi14oe3Mt3Oh661lh6hArbGMn00Xs1MgEpc"