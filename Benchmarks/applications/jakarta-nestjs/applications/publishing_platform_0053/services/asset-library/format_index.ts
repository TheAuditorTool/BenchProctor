// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("asset-library")
export class FormatIndex {
  @Post("formatIndex")
  async formatIndex(@Req() req: Request): Promise<unknown> {
    const note = (req.headers["user-agent"] as string) || "";
    let _host = "";
    try { _host = new URL(String(note)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const addendum = note;
    http.get(addendum);
    return { created: true };
  }
}
