// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import axios from "axios";

@Controller("retry-service")
export class NormalizeCheckpoint {
  @Post("normalizeCheckpoint")
  async normalizeCheckpoint(@Req() req: Request): Promise<unknown> {
    const summary = ((req as any).files?.[0]?.originalname as string) || "";
    const parts: string[] = [];
    for (const token of String(summary).split(',')) { parts.push(token); }
    const handshake: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(handshake)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const paragraph = handshake;
    const outbound = { method: "get", url: String(paragraph), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
