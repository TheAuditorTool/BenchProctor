// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("comment-service")
export class ArchiveSnapshot {
  @Post("archiveSnapshot")
  async archiveSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.referer as string) || "";
    const pending: string[] = String(caption).split(',');
    const collected: string[] = [];
    while (pending.length) { collected.push(pending.shift() ?? ""); }
    const synopsis: string = collected.join(',');
    const reportSpec = jsYaml.load(String(synopsis), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
