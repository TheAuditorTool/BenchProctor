// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("registry-service")
export class AnnotateWindow {
  @Post("annotateWindow")
  async annotateWindow(@Req() req: Request): Promise<unknown> {
    const subtitle = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(subtitle)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const handshake = subtitle;
    http.get(handshake);
    return { created: true };
  }
}
