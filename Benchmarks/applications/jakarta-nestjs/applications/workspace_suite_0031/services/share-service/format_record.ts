// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("share-service")
export class FormatRecord {
  @Post("formatRecord")
  async formatRecord(@Req() req: Request): Promise<unknown> {
    const caption = (req.cookies?.session_token as string) || "";
    const [synopsis] = String(caption).split(',');
    const reportSpec = jsYaml.load(String(synopsis), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
