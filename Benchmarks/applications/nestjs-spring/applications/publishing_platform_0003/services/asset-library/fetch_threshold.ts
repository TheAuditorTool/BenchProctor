// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, ForbiddenException } from "@nestjs/common";
import { Request } from "express";
import * as shared from "./shared";
import axios from "axios";

@Controller("asset-library")
export class FetchThreshold {
  @Post("fetchThreshold")
  async fetchThreshold(@Req() req: Request): Promise<unknown> {
    const heading = (await shared.mq.receive("app-events"));
    const transform = (v: string): string => v.trim();
    const addendum: string = transform(heading);
    let _host = "";
    try { _host = new URL(String(addendum)).hostname; } catch (e) { throw new ForbiddenException({error:"host not allowed"}); }
    if (!/^(api\.trustmesh\.internal|assets\.trustcdn\.io)$/.test(_host)) { throw new ForbiddenException({error:"host not allowed"}); }
    const byline = addendum;
    const outbound = { method: "get", url: String(byline), timeout: 5000 };
    await axios.request(outbound);
    return { created: true };
  }
}
