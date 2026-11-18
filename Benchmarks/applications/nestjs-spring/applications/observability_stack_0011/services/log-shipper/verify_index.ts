// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("log-shipper")
export class VerifyIndex {
  @Post("verifyIndex")
  async verifyIndex(@Req() req: Request): Promise<unknown> {
    const caption = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(caption).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    http.get(cohort);
    return { created: true };
  }
}
