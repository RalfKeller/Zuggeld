import { Injectable } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

declare var $ : any
@Injectable()
export class CommService {

    constructor(private http : HttpClient) { }

    getDelays() : Observable<Delay[]> {
        let user : User = {
            anrede: "Herr",
            vorname: "Ralf",
            name: "Keller",
            strasse : "Asd",
            strasse_nr : "33",
            staat : "DE",
            plz : "33098",
            wohnort : "PB",
            konto_inhaber : "Ich",
            iban : "123",
            bic : "GEN",
            datum_unterschrift : "19.12.1990",
            unterschrift : "AAA",
            ticket_bild : "Bild",
            mail : ""            
        }

        console.log(user)
        let observable : Observable<Delay[]> = this.http.get<Delay[]>('http://bahngeld.de/getData.php')
        return observable;
    }

    postData(user : User, selectedDelays : number[]) {
        let params : HttpParams = new HttpParams()
        
        params = params.append('jsonUser', JSON.stringify(user))
        params.append('jsonDelays', JSON.stringify(selectedDelays))
        this.http.post('http://bahngeld.de/submit.php', params).subscribe(data => console.log(data), error => console.log(error))
    }
    
}