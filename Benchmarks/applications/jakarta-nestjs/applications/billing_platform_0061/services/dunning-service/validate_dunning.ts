// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("dunning-service")
export class ValidateDunning {
  @Post("validateDunning")
  async validateDunning(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const remittance = Buffer.from(footnote, "utf-8").toString();
    let _host = "";
    try { _host = new URL(String(remittance)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const arrears = remittance;
    http.get(arrears);
    return { created: true };
  }
}
