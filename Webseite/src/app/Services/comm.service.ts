import { Injectable } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class CommService {

    constructor(private http : HttpClient) { }

    getDelays() : Observable<Delay[]> {
        return this.http.get<Delay[]>('assets/delays.json')
    }

    postData(ids : number[], vorname : string, nachname : string, street : string, hausnummer : number, plz : number, wohnort : string, email : string) {
        let idString : string = ""
        for(let id of ids) {
            idString += id + " "
        }

        let params : HttpParams = new HttpParams()
        params.append('ids', idString)
        params.append('vorname', vorname)
        params.append('nachname', nachname)
        params.append('email', email)
        params.append('street', street)
        params.append('hausnummer', hausnummer + "")
        params.append('plz', plz + "")

        this.http.post('zuggeld.de/php/submit.php', params)
    }
    
}