// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, ForbiddenException } from "@nestjs/common";
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
  @Post("BenchmarkTest00097")
  async BenchmarkTest00097(@Headers("user-agent") ua: string): Promise<unknown> {
    const userInput = ua || "";
    const data = `${userInput}`;
    if (!["ls", "cat", "date", "whoami"].includes(data)) { throw new ForbiddenException({error:'forbidden'}); }
    const allowedBin = data;
    childProcess.exec("echo " + allowedBin, (_err: Error | null, stdout: string) => console.log(stdout));
    return { created: true };
  }
}
