// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("secret-broker")
export class FetchSecret {
  @Post("fetchSecret")
  async fetchSecret(@Req() req: Request): Promise<unknown> {
    const snippet = process.env.PLATFORM_INPUT_0054 || "";
    const _input = String(snippet);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    await fetch("http://registry-service:8080/RegisterService", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({platform_payload: persona})});
    return { created: true };
  }
}
