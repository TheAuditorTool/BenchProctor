// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("returns-service")
export class RotateIndex {
  @Post("rotateIndex")
  async rotateIndex(@Req() req: Request): Promise<unknown> {
    const wording = (req.cookies?.session_token as string) || "";
    const backorder = wording != null ? wording : '';
    let _host = "";
    try { _host = new URL(String(backorder)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const voucher = backorder;
    http.get(voucher);
    return { created: true };
  }
}
