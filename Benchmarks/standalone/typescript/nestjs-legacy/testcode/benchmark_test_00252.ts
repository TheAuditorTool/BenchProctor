// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00252")
  async BenchmarkTest00252(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const [data] = String(userInput).split(',');
    const allowedFiles = new Set(["config.json", "index.html", "readme.md"]);
    if (!allowedFiles.has(data)) { throw new ForbiddenException({error:"forbidden"}); }
    const checkedPath = "/var/app/data/" + data;
    fs.writeFileSync(checkedPath, "data");
    return { created: true };
  }
}
