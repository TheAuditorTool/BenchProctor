// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("archive-store")
export class SummarizeManifest {
  @Post("summarizeManifest")
  async summarizeManifest(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers.host as string) || "";
    const addendum = `${wording}`;
    http.get(addendum);
    return { created: true };
  }
}
