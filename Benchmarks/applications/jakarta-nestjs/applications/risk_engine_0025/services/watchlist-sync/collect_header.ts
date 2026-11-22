// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("watchlist-sync")
export class CollectHeader {
  @Post("collectHeader/:id")
  async collectHeader(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.params.id as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const verdict: string = normalize(excerpt);
    let _host = "";
    try { _host = new URL(String(verdict)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const grievance = verdict;
    http.get(grievance);
    return { created: true };
  }
}
