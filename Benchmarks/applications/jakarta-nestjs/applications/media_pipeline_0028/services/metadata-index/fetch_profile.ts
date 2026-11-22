// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metadata-index")
export class FetchProfile {
  @Post("fetchProfile")
  async fetchProfile(@Req() req: Request): Promise<unknown> {
    const citation = (req.body as string) || "";
    const _raw = citation;
    const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + rendition, "data");
    return { created: true };
  }
}
