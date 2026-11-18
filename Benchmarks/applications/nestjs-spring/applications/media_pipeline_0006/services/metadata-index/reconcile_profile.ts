// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("metadata-index")
export class ReconcileProfile {
  @Post("reconcileProfile")
  async reconcileProfile(@Req() req: Request): Promise<unknown> {
    const passage = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(passage);
    const montage: string = readInput();
    let _host = "";
    try { _host = new URL(String(montage)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const rendition = montage;
    http.get(rendition);
    return { created: true };
  }
}
