// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("platform-api")
export class ValidateBundle {
  @Post("validateBundle")
  async validateBundle(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.origin as string) || "";
    const _input = String(note);
    let handshake;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': handshake = _input.normalize('NFC'); break;
      default: handshake = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const persona = handshake;
    http.get(persona);
    return { created: true };
  }
}
