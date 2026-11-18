// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("archive-store")
export class VerifyConversion {
  @Post("verifyConversion")
  async verifyConversion(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(note);
    const addendum: string = readInput();
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    http.get(dossier);
    return { created: true };
  }
}
