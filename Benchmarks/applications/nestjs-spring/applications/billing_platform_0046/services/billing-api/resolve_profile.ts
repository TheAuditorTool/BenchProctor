// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import * as http from "http";

@Controller("billing-api")
export class ResolveProfile {
  @Post("resolveProfile")
  async resolveProfile(@Req() req: Request): Promise<unknown> {
    const remark = (await shared.mq.receive("app-events"));
    const parts: string[] = [];
    for (const token of String(remark).split(',')) { parts.push(token); }
    const remittance: string = parts.join(',');
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const arrears = remittance;
    http.get(arrears);
    return { created: true };
  }
}
