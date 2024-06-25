## generate public & private key pair in ur computer
- open Git Bash (here use this way "ed25519" to gen the pair key,can also use "rsa" instead )

```bash=
$ ssh-keygen -t ed25519 -C "your gituser email" 

# Generating public/private ed25519 key pair.
Enter file in which to save the key (/c/Users/User/.ssh/id_ed25519): /c/Users/User/.ssh/id_ed25519

# (密碼短語 我有設定/OPTIONAL)Enter passphrase (empty for no passphrase):

# Your identification has been saved in /c/Users/User/.ssh/id_ed25519 (PRIVATE KEY)
# Your public key has been saved in /c/Users/User/.ssh/id_ed25519.pub (PUBLIC KEY)

```

- 去.ssh檔案夾看一下剛剛生成的key pair檔案
```bash=
$ cd /c/Users/User/.ssh/
$ ls
# 會看到至少剛剛生成的key pair .pub結尾的是PUBLIC KEY
# id_ed25519  id_ed25519.pub
```

- 複製public key 
```bash=
$ cat ~/.ssh/id_ed25519.pub | clip

# =>再進到Gitgub個人頁面的設定中=>添加ssh key =>貼上public key
```

- 啟動ssh代理,並添加ssh 私鑰到agent:
```bash=
$ eval "$(ssh-agent -s)"  ssh-add ~/.ssh/id_ed25519

# Agent pid 1594
# (輸入密碼短語 如果有設置)Enter passphrase for /c/Users/User/.ssh/id_ed25519:
# Identity added: /c/Users/User/.ssh/id_ed25519 (會顯示email)
```

- 測試ssh連線Github
```bash=
$ ssh -T git@github.com
# Hi "我的名字"! You've successfully authenticated, but GitHub does not provide shell access.
```

- 現在可以用ssh連線github上傳自己的專案版控