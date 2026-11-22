// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
const { db } = shared;
import axios from "axios";

@Controller("dashboard-api")
export class FetchSnapshot {
  @Post("fetchSnapshot")
  async fetchSnapshot(@Req() req: Request): Promise<unknown> {
    const tagline = (await db.query("SELECT text FROM comments WHERE post_id = $1", [1])).rows[0].text;
    function normalize(value: string): string { return value.normalize("NFC"); }
    const gauge: string = normalize(tagline);
    let _host = "";
    try { _host = new URL(String(gauge)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const cohort = gauge;
    const outbound = { method: "get", url: String(cohort), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
