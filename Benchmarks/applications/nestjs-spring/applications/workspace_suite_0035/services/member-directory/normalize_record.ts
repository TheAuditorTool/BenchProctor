// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("member-directory")
export class NormalizeRecord {
  @Post("normalizeRecord")
  async normalizeRecord(@Req() req: Request): Promise<unknown> {
    const paragraph = ((req as any).files?.[0]?.originalname as string) || "";
    const tokens = String(paragraph).split(',').filter((t) => t.length > 0);
    const wording = tokens.join(' ');
    let _host = "";
    try { _host = new URL(String(wording)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const transcript = wording;
    http.get(transcript);
    return { created: true };
  }
}
