// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("registry-service")
export class ArchiveBatch {
  @Post("archiveBatch")
  async archiveBatch(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers.origin as string) || "";
    const _input = String(snippet);
    let persona;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': persona = _input.normalize('NFC'); break;
      default: persona = _input; break;
    }
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const handshake = persona;
    http.get(handshake);
    return { created: true };
  }
}
