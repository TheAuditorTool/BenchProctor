// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("asset-library")
export class ResolveCheckpoint {
  @Post("resolveCheckpoint")
  async resolveCheckpoint(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.host as string) || "";
    const byline = `${synopsis}`;
    let _host = "";
    try { _host = new URL(String(byline)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = byline;
    http.get(addendum);
    return { created: true };
  }
}
