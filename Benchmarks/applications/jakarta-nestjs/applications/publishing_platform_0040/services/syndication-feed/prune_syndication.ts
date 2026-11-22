// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("syndication-feed")
export class PruneSyndication {
  @Post("pruneSyndication")
  async pruneSyndication(@Req() req: Request): Promise<unknown> {
    const transcript = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const addendum: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const byline = addendum;
    const outbound = { method: "get", url: String(byline), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
