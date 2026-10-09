AUTH_LOG = [
"Oct 7 09:12:03 srv-web sshd[2101]: Accepted password for Chris from 192.0.2.10 port 50122 ssh2",
"Oct 7 09:40:17 srv-web sshd[2144]: Failed password for Manon from 192.0.2.25 port 50388 ssh2",
"Oct 7 09:40:29 srv-web sshd[2144]: Accepted password for Manon from 192.0.2.25 port 50388 ssh2",
"Oct 7 10:02:11 srv-web sshd[2210]: Failed password for root from 203.0.113.45 port 51122 ssh2",
"Oct 7 10:02:14 srv-web sshd[2212]: Failed password for root from 203.0.113.45 port 51130 ssh2",
"Oct 7 10:02:18 srv-web sshd[2215]: Failed password for invalid user admin from 203.0.113.45 port 51141 ssh2",
"Oct 7 10:02:21 srv-web sshd[2218]: Failed password for invalid user test from 203.0.113.45 port 51150 ssh2",
"Oct 7 10:02:25 srv-web sshd[2221]: Failed password for Chris from 203.0.113.45 port 51162 ssh2",
"Oct 7 10:02:29 srv-web sshd[2224]: Failed password for Chris from 203.0.113.45 port 51170 ssh2",
"Oct 7 10:02:33 srv-web sshd[2227]: Failed password for Chris from 203.0.113.45 port 51178 ssh2",
"Oct 7 10:02:36 srv-web sshd[2230]: Accepted password for Chris from 203.0.113.45 port 51185 ssh2",
"Oct 7 10:02:37 srv-web sshd[2230]: pam_unix(sshd:session): session opened for user Chris by (uid=0)",
"Oct 7 10:15:40 srv-web sshd[2301]: Failed password for invalid user oracle from 198.51.100.23 port 40022 ssh2",
"Oct 7 10:15:44 srv-web sshd[2303]: Failed password for invalid user postgres from 198.51.100.23 port 40031 ssh2",
"Oct 7 10:15:47 srv-web sshd[2305]: Failed password for root from 198.51.100.23 port 40040 ssh2",
"Oct 7 10:15:51 srv-web sshd[2307]: Failed password for invalid user ubuntu from 198.51.100.23 port 40052 ssh2",
"Oct 7 10:15:55 srv-web sshd[2309]: Failed password for invalid user pi from 198.51.100.23 port 40060 ssh2",
"Oct 7 10:16:02 srv-web sshd[2311]: Connection closed by 198.51.100.23 port 40071 [preauth]",
"Oct 7 11:30:08 srv-web sshd[2402]: Failed password for Cosmo from 198.51.100.77 port 42210 ssh2",
"Oct 7 11:30:15 srv-web sshd[2404]: Failed password for Cosmo from 198.51.100.77 port 42218 ssh2",
"Oct 7 11:31:02 srv-web sshd[2410]: Accepted password for Cosmo from 198.51.100.77 port 42230 ssh2",
]

def count_failures(lines):
    failures = {}  # Stocke le nombre d'échecs pour chaque IP
    
    for line in lines:

        # On garde seulement les tentatives échouées
        if "Failed password" in line:
            words = line.split()

            # L'adresse IP se trouve juste après le mot "from"
            index_from = words.index("from")
            ip = words[index_from + 1]

            # Ajoute 1 échec à cette IP
            failures[ip] = failures.get(ip, 0) + 1

    return failures
   
def detect_brute_force(lines, threshold=5):
    failures = count_failures(lines)
    detected = []
    
    # Vérifie quelles IP dépassent le seuil
    for ip, count in failures.items():
        if count >= threshold:
            detected.append(ip)

    return detected

def print_report(lines, threshold=5):
    failures = count_failures(lines)
    detected = detect_brute_force(lines, threshold)

 # Affiche une alerte pour chaque IP détectée
    for ip in detected:
        print(f"[ALERTE] {ip} : {failures[ip]} échecs d'authentification")

# Tests demandés dans le TP
print(count_failures(AUTH_LOG))
print(detect_brute_force(AUTH_LOG))
print(detect_brute_force(AUTH_LOG, threshold=2))
print_report(AUTH_LOG)