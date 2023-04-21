/*
**  server.c
**  
**  Esempio di comunicazione via socket.
**  Componente server. Ascolta sull'indirizzo di
**  loopback (127.0.0.1) sulla porta TCP 12345.
**
**  #(@)20150312(liverani@mat.uniroma3.it)
*/

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

#define SERVERPORT 12345
#define SERVERADDRESS ""
#define MAX 32

int main(int argc, char * argv[]) {
  int serverSocket, connectSocket, returnCode;
  socklen_t clientAddressLen;
  struct sockaddr_in serverAddress, clientAddress;
  char buffer[MAX];
  char *clientIP;
  
  
  /* apertura socket del server */
  if (((serverSocket = socket(AF_INET,SOCK_STREAM,0))) == -1) {
    perror("Error in server socket()");
    exit(-1);
  }
    
  /* preparazione dell'indirizzo locale del server */
  serverAddress.sin_family = AF_INET;
  serverAddress.sin_port = htons(SERVERPORT);
  serverAddress.sin_addr.s_addr = inet_addr(SERVERADDRESS);
  
  /* bind del socket */
  if ((returnCode = bind (serverSocket, (struct sockaddr*)  &serverAddress, sizeof(serverAddress))) == -1) {
    perror("Error in server socket bind()");
    exit(-1);
  }
  
  /* listen del socket */
  if ((returnCode = listen(serverSocket, 1)) == -1) {
    perror("Error in server socket listen()");
    exit(-1);
  }
  
  printf("Server ready (CTRL-C per terminare)\n");
  
  clientAddressLen = sizeof(clientAddress);
  
  /* ciclo infinito in attesa di connessione */
  while (1) {

    /* accetta le connessioni */
    if ((connectSocket = accept(serverSocket, (struct sockaddr *)&clientAddress, &clientAddressLen)) == -1) {
      perror("Error in accept()");
      close(serverSocket);
      exit(-1);
    }
    
    /* memorizzo l'indirizzo del client in formato stringa */
    clientIP = inet_ntoa(clientAddress.sin_addr);
    
    printf("\nClient @ %s connects on socket %d\n", clientIP, connectSocket);
    
    /* riceve i messaggi e li stampa in output */
    while ((returnCode = read(connectSocket, buffer, MAX-1)) > 0) {
      buffer[returnCode] = '\0'; // buffer dev'essere una stringa e va terminata con '\0'
      FILE *fp = fopen("attiva.txt","w");
      if (fp == NULL)
        {
          perror("errore");
          exit(1);
        }
      fprintf(fp,"%s",buffer);
      fclose(fp);
      printf(">> %s: allarme: %s\n", clientIP, buffer);
    }
    
    /* chiudo il socket */
    close(connectSocket);
  }
  return(0);
}
