// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("artifact-store")
export class PublishRecord {
  @Post("publishRecord")
  async publishRecord(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const note: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(note)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const phrase = note;
    http.get(phrase);
    return { created: true };
  }
}
