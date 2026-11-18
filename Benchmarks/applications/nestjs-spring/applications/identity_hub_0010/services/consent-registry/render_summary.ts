// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("consent-registry")
export class RenderSummary {
  @Post("renderSummary")
  async renderSummary(@Req() req: Request): Promise<unknown> {
    const phrase = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(phrase).split(',')) { parts.push(token); }
    const persona: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(persona)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const transcript = persona;
    http.get(transcript);
    return { created: true };
  }
}
