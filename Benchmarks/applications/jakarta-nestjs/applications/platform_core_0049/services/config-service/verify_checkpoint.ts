// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("config-service")
export class VerifyCheckpoint {
  @Post("verifyCheckpoint")
  async verifyCheckpoint(@Req() req: Request): Promise<unknown> {
    const notice = (req.body as string) || "";
    const persona = Buffer.from(notice, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const handshake = persona;
    http.get(handshake);
    return { created: true };
  }
}
