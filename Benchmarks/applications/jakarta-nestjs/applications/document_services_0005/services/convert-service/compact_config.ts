// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("convert-service")
export class CompactConfig {
  @Post("compactConfig/:id")
  async compactConfig(@Req() req: Request): Promise<unknown> {
    const footnote = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const addendum: string = normalize(footnote);
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const dossier = addendum;
    http.get(dossier);
    return { created: true };
  }
}
