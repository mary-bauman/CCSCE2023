import java.util.*;
public class Eight {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int test = Integer.valueOf(sc.nextLine());
        for(int a = 0; a < test; a++){
            String s = sc.nextLine();
            int c = 0;
            int lenVar = s.length();
            while(c<lenVar){
                if(s.charAt(c)=='a'){
                    s = s.substring(0,c) + "e" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='e'){
                    s = s.substring(0,c) + "i" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='i'){
                    s = s.substring(0,c) + "o" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='o'){
                    s = s.substring(0,c) + "u" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='u'){
                    s = s.substring(0,c) + "a" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='A'){
                    s = s.substring(0,c) + "E" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='E'){
                    s = s.substring(0,c) + "I" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='I'){
                    s = s.substring(0,c) + "O" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='O'){
                    s = s.substring(0,c) + "U" + s.substring(c+1,s.length());
                }
                else if(s.charAt(c)=='U'){
                    s = s.substring(0,c) + "A" + s.substring(c+1,s.length());
                }
                else if(Character.isAlphabetic(s.charAt(c))){
                    int x = (s.charAt(c) + 1);
                    char ch = (char)x;
                    if(s.charAt(c)=='z'){
                        ch = 'b';
                    }
                    if(s.charAt(c)=='Z'){
                        ch = 'B';
                    }
                    //s = s.substring(0,c) + sx + s.substring(c+1,s.length());
                    String newS = "";
                    newS = s.substring(0,c);
                    newS = newS + ch;
                    newS = newS + s.substring(c+1,s.length());
                    s = newS;
                }
                c = c + 1;
            }



            System.out.println(s);
        }
        
    }
}