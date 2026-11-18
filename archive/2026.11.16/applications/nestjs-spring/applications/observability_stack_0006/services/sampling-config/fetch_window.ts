// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("sampling-config")
export class FetchWindow {
  @Post("fetchWindow/:id")
  async fetchWindow(@Req() req: Request): Promise<unknown> {
    const preface = (req.params.id as string) || "";
    const cohort = preface != null ? preface : '';
    let _host = "";
    try { _host = new URL(String(cohort)).hostname; } catch (e) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const _addr = (await require("dns").promises.lookup(_host)).address;
    if (/^(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.|::1$|::[fF]{4}:(0\.|10\.|127\.|169\.254\.|192\.168\.|172\.(1[6-9]|2[0-9]|3[01])\.)|[fF][cCdD]|[fF][eE]80:)/.test(_addr)) { throw new ForbiddenException({error:"private or loopback address not allowed"}); }
    const gauge = cohort;
    http.get(gauge);
    return { created: true };
  }
}
