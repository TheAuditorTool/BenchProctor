// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("stream-packager")
export class ArchiveRecord {
  @Post("archiveRecord")
  async archiveRecord(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.body?.variables?.input as string) || "";
    const parts: string[] = [];
    for (const token of String(synopsis).split(',')) { parts.push(token); }
    const rendition: string = parts.join(',');
    const reportSpec = jsYaml.load(String(rendition), { schema: jsYaml.CORE_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
