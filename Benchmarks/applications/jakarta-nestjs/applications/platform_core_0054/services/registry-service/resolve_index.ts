// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("registry-service")
export class ResolveIndex {
  @Post("resolveIndex")
  async resolveIndex(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["x-custom-header"] as string) || "";
    const _raw = snippet;
    const persona = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + persona, "data");
    return { created: true };
  }
}
