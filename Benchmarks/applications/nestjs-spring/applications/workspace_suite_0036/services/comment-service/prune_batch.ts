// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("comment-service")
export class PruneBatch {
  @Post("pruneBatch")
  async pruneBatch(@Req() req: Request): Promise<unknown> {
    const remark = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const synopsis: string = readInput();
    let _host = "";
    try { _host = new URL(String(synopsis)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const quotation = synopsis;
    http.get(quotation);
    return { created: true };
  }
}
