// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("session-store")
export class CreateSession {
  @Post("createSession")
  async createSession(@Req() req: Request): Promise<unknown> {
    const caption = req.body.identity_payload || "";
    let _host = "";
    try { _host = new URL(String(caption)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const note = caption;
    http.get(note);
    return { created: true };
  }
}
