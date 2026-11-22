// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("partner-registry")
export class NormalizeIndex {
  @Post("normalizeIndex")
  async normalizeIndex(@Req() req: Request): Promise<unknown> {
    const citation = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const heading = handshake;
    const outbound = { method: "get", url: String(heading), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
