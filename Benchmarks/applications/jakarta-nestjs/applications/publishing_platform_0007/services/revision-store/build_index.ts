// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("revision-store")
export class BuildIndex {
  @Post("buildIndex")
  async buildIndex(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers["user-agent"] as string) || "";
    http.get(remark);
    return { created: true };
  }
}
