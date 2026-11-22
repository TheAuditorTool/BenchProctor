// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("upload-gateway")
export class ExportProfile {
  @Post("exportProfile")
  async exportProfile(@Req() req: Request): Promise<unknown> {
    const synopsis = (req.headers.origin as string) || "";
    const _raw = synopsis;
    const rendition = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(rendition), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
