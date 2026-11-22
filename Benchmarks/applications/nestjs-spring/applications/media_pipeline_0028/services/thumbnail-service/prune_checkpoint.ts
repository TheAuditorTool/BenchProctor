// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("thumbnail-service")
export class PruneCheckpoint {
  @Post("pruneCheckpoint")
  async pruneCheckpoint(@Req() req: Request): Promise<unknown> {
    const citation = (req.cookies?.session_token as string) || "";
    const parts: string[] = [];
    for (const token of String(citation).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(rendition)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const montage = rendition;
    http.get(montage);
    return { created: true };
  }
}
