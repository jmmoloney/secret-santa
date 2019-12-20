# secret-santa
Secret Santa Email Script made for groups who can't get together to draw names.  

## Setup
Set up the following files in the correct format. Example files are given in the repo.  

- `guest_list.csv`  
  - CSV of the names and emails of the guests attending
- `couples.csv` (optional)
   - Optional CSV of pairs of couples attending
   - If missing or blank, skips check that couples do not draw each other

## Usage
With your files set up, run the script with the following command. Please include a random seed as this
will help you re-run the script with the same results should you need to.  
You'll be prompted for your password.


```python3 secret_santa.py <sender_gmail_address> <seed>```  

You will have to allow "Less Secure" apps access to the sender gmail address.
This isn't generally advised as it drops a lot of Gmail's security around your
account. It might be better to use a throwaway address.

Visit your Google Account and turn on 'Allow less secure apps' [here](https://myaccount.google.com/lesssecureapps). For more detailed instructions see this post on devanswers.co, [Allow less secure apps to access your Gmail account] (https://devanswers.co/allow-less-secure-apps-access-gmail-account/).
