// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, ForbiddenException } from "@nestjs/common";
import { Response } from "express";
import * as childProcess from "child_process";
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
  @Post("BenchmarkTest00147")
  async BenchmarkTest00147(@Body("field") field: string): Promise<unknown> {
    const userInput = field || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const data: string = normalize(userInput);
    if (!["ls", "cat", "date", "whoami"].includes(data)) { throw new ForbiddenException({error:'forbidden'}); }
    const allowedBin = data;
    childProcess.spawn("echo " + allowedBin, { shell: true, stdio: "inherit" });
    return { created: true };
  }
}
