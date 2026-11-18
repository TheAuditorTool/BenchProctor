// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("revision-store")
export class PublishManifest {
  @Post("publishManifest")
  async publishManifest(@Req() req: Request): Promise<unknown> {
    const footnote = (req.headers.host as string) || "";
    const byline = `${footnote}`;
    http.get(byline);
    return { created: true };
  }
}
