// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("settlement-service")
export class MergeConfig {
  @Post("mergeConfig")
  async mergeConfig(@Req() req: Request): Promise<unknown> {
    const remark = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dunning = remittance;
    http.get(dunning);
    return { created: true };
  }
}
